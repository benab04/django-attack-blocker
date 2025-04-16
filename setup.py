from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-attack-blocker",
    version="0.1.0",
    author="Ben Abraham Biju",
    author_email="benabrahambiju@gmail.com",
    description="ML-based IP blocking system for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/django-ml-ipblocker",
    packages=find_packages(),
    package_data={
        'django_ml_ipblocker': [
            'models/*.pkl', 
            'models/*.joblib'
        ],
    },
    include_package_data=True,  # This is important
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
    ],
    python_requires=">=3.6",
    install_requires=[
        "django>=3.2",
        "pandas",
        "numpy",
        "scikit-learn",
        "joblib",
    ],
)