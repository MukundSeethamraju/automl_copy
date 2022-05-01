from distutils.core import setup

setup(
    name='automl_efficientdet',
    version='0.0.1',
    author='X.X',
    url='https://github.com/google/automl',
    license='LICENSE',
    packages=['efficientdet'],
    description='converting google\'s automl repo into a python package',
    install_requires=[
      "absl==0.0",
      "absl_py==0.12.0",
      "lxml==4.7.1",
      "matplotlib",
      "neural_structured_learning==1.3.1",
      "pycocotools==2.0.4",
      "PyYAML==6.0",
      "six",
      "tensorflow_addons",
      "tensorflow_datasets==4.4.0",
      "tensorflow_hub==0.12.0",
      "tensorflow_model_optimization==0.7.0"
    ]
)
