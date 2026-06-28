# OptiCrop — Smart Agricultural Production Optimization Engine

OptiCrop is a machine-learning powered web app that recommends the most suitable
crop for a given set of soil and climate conditions. A user enters Nitrogen (N),
Phosphorous (P), Potassium (K), temperature, humidity, pH, and rainfall values,
and the app returns the crop best suited to those exact conditions.

**Live repository**: https://github.com/neelimavana/OptiCrop

## Problem statement

Farmers often choose crops based on tradition or general regional advice rather
than the actual measured soil and climate conditions on their land, which leads
to lower yields and wasted resources. OptiCrop replaces that guesswork with a
trained classifier that maps soil/climate inputs directly to a crop recommendation.

## Tech stack

- **ML**: NumPy, Pandas, Scikit-learn, SciPy
- **Visualization**: Matplotlib, Seaborn
- **Web**: Flask
- **Dataset**: [Crop Recommendation Dataset](https://www.kaggle.com/datasets/chitrakumari25/smart-agricultural-production-optimizing-engine) — N, P, K, temperature, humidity, ph, rainfall → label (22 balanced crop classes, 100 samples each)

## Repository structure