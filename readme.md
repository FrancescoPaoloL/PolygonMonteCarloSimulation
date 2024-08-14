# Polygon MonteCarlo Simulation
Here we have an implementation of the Monte Carlo method to estimate the area of an irregular figure inside a square. The Monte Carlo method involves generating random points within the square and determining the proportion that fall inside the irregular figure.

To estimate the area of the irregular figure, use the following formula:

    Estimated Area of Irregular Figure = (Number of Points Inside Irregular Figure / Total Number of Points Inside Square) × Area of Square

In practice we:

- Generate many random points within a square that surrounds the shape.
- Count how many points fall inside the irregular shape.
- Estimate the area of the shape based on the ratio of points inside it compared to the total number of points.

![example](https://github.com/user-attachments/assets/77bf6718-014b-4174-8f3e-7abe873085db)

Please note than in `save_irregular_points.py` we use the NPY format because it's faster compared to other formats. 
It's true that the benefits are minimal, but consider it a best practice.

## Languages and Tools
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

## Requirements
```
matplotlib==3.6.3
numpy==1.24.2
```

## Test Coverage
TODO

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>

