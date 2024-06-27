# Lib-ML
Internal tools for the ML backend. Includes preproccesing of URLs. Versions [model-training](https://github.com/remla24-team-1/model-training) and [model-service](https://github.com/remla24-team-1/model-service/).

If you wish to test the package, you can install it locally through `$ pip install remlapreprocesspy`. You can also install it by running `poetry install` from within the lib-ml folder.

## Example usage
```
# python
import remlapreprocesspy
print(preprocess(["test.org","www.test.com"]))
```

## Release instructions

To release an updated version, set the version variable within the `pyproject.toml` and push a tag with the same version number. For example, to release VX.X.X, set `version = X.X.X` in `pyproject.toml`. Then add the new tag through `git tag VX.X.X` and push the tag using `git push origin tag VX.X.X`. The new version will be automatically published to PyPI by the github workflow.
