from distutils.core import setup, find_packages

setup(
    name='automl_efficientdet',
    version='0.0.1',
    author='X.X',
    url='https://github.com/google/automl',
    license='LICENSE',
    packages=find_packages(),
    description='converting google\'s automl repo into a python package',
    install_requires=[
      "absl-py",
      "absl_py==0.12.0",
      "lxml==4.7.1",
      "matplotlib",
      "neural_structured_learning==1.3.1",
      "pycocotools==2.0.4",
      "PyYAML==6.0",
      "six",
      "tensorflow==2.5.0",
      "tensorflow_addons==0.13.0",
      "tensorflow_datasets==4.4.0",
      "tensorflow_hub==0.12.0",
      "tensorflow_model_optimization==0.7.0"
    ]
)
