import pandas as pd
import patsy

from sklearn import linear_model

from pylab import *

df = pd.read_csv('train.csv') # Get this from kaggle: https://www.kaggle.com/c/titanic

df.head()

df.groupby('Survived').mean()

k = df.groupby([pd.cut(df.Age, np.linspace(0, 100, 15))]).mean()
plot(k.Age, k.Survived)


y, X = patsy.dmatrices('Survived ~ Age + Sex + Fare', data=df)

mdl = linear_model.LogisticRegression()
f = mdl.fit(X, y)

plot(y, f.predict(X), '.')

from sklearn.model_selection import cross_val_score
scores = cross_val_score(mdl, X, y.ravel(), cv=5)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

classifiers = {
    'LogisticRegression': mdl,
    'LDA': LinearDiscriminantAnalysis(),
    'SVM': SVC(kernel='rbf'),
    'Tree': DecisionTreeClassifier(),
    'Forest': RandomForestClassifier()
}

for name, clf in classifiers.items():
    print(name, cross_val_score(clf, X, y.ravel(), cv=5).mean())


from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
estimators = [('reduce_dim', PCA(n_components=3)),
              ('clf', LinearDiscriminantAnalysis())]

classifiers['LDA'] = Pipeline(estimators)
for name, clf in classifiers.items():
    print(name, cross_val_score(clf, X, y.ravel(), cv=5).mean())


from joblib import memory
Memory = memory.Memory(cachedir='.')


@Memory.cache
def foo(clf, X, y):
    return cross_val_score(clf, X, y.ravel(), cv=5).mean()

for name, clf in classifiers.items():
    print(name, foo(clf, X, y))


import pymc3 as pm
plt.style.use('seaborn-ticks')
drug = np.random.randn(25) + 0.5
placebo = np.random.randn(25)*1.5

y1 = np.array(drug)
y2 = np.array(placebo)
y = pd.DataFrame(dict(value=np.r_[y1, y2], group=np.r_[
                 ['drug'] * len(drug), ['placebo'] * len(placebo)]))


# Center prior on empirical means and larger std.
μ_m = y.value.mean()
μ_s = y.value.std() * 2

# Set prior for standard deviations to uniform distribution
σ_low = 0.1
σ_high = 10

with pm.Model() as model:
    group1_mean = pm.Normal('group1_mean', μ_m, sd=μ_s)
    group2_mean = pm.Normal('group2_mean', μ_m, sd=μ_s)

    group1_std = pm.Uniform('group1_std', lower=σ_low, upper=σ_high)
    group2_std = pm.Uniform('group2_std', lower=σ_low, upper=σ_high)

    ν = pm.Exponential('ν_minus_one', 1 / 29.) + 1

    λ1 = group1_std**-2 # Convert to precision
    λ2 = group2_std**-2

    group1 = pm.StudentT('drug', nu=ν, mu=group1_mean, lam=λ1, observed=y1)
    group2 = pm.StudentT('placebo', nu=ν, mu=group2_mean, lam=λ2, observed=y2)
    diff_of_means = pm.Deterministic(
        'difference of means', group1_mean - group2_mean)
    diff_of_stds = pm.Deterministic(
        'difference of stds', group1_std - group2_std)
    effect_size = pm.Deterministic('effect size',
                                   diff_of_means / np.sqrt((group1_std**2 + group2_std**2) / 2))


with model:
    trace = pm.sample(2000, cores=2)

pm.plot_posterior(trace, varnames=['difference of means','difference of stds', 'effect size'],
                  ref_val=0,
                  color='#87ceeb')