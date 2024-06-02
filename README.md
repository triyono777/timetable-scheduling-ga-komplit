# Solving a University Scheduling Problem with Genetic Algorithms
## Group: *Pastéis de Data*
![image](https://github.com/MajdAlAjlaniiii/timetable-ga/assets/143721521/b901f69c-2059-42e9-b6fc-8b7f3b363715)
- Diogo Pires, 20230534
- Majd Al Ajlani, 20230767
- Manuel Gonçalves, 20230466
- Maria Batrakova, 20230739

Welcome to our Computational Intelligence for Optimization project! This project employs Genetic Algorithms (GAs) to solve a University Scheduling problem. GAs are search heuristics inspired by the process of natural evolution, used to generate high-quality solutions for optimization and search problems.

## Project Overview

By encoding potential timetables as chromosomes, GAs will evolve these solutions through selection, crossover, and mutation operations. The goal of this project is to develop a timetable that satisfies all hard constraints, such as preventing overlaps, and optimizing soft constraints, like accounting for Professor’s preferences. Through iterative improvement, the GA aims to find the most efficient and practical scheduling arrangement for our university courses.

## Directory Structure

The project is organized into the following directories and files:

```
├── DataStructure
│   ├── Class.py
│   ├── Course.py
│   ├── Department.py
│   ├── Population.py
│   ├── Professor.py
│   ├── Room.py
│   ├── Schedule.py
│   ├── Timeslot.py
├── Experiments
│   ├── experimental_comparison.py
│   ├── experimental_comparison_CI.py
│   ├── penalties_comparison.py
├── GeneticAlgorithmComponents
│   ├── crossover.py
│   ├── genetic_algorithm.py
│   ├── mutation.py
│   ├── selection.py
├── Utils
│   ├── constants.py
│   ├── display.py
├── data.py
├── main.py
├── README.md
├── PasteisDeData.pdf
```

## File Descriptions

### DataStructure Folder

- `Class.py`: Represents a scheduled class, including department, course, assigned professor, timeslot, and room.
- `Course.py`: Manages course details, including course number, name, associated professors, maximum number of students, and preferred timeslots and rooms.
- `Department.py`: Manages department details, including name and associated courses.
- `Population.py`: Handles the population of schedules for the GA.
- `Professor.py`: Manages professor-specific data and preferences.
- `Room.py`: Manages the room details, including number and capacity.
- `Schedule.py`: Defines the scheduling logic, fitness and constraints.
- `Timeslot.py`: Manages timeslot-specific data.

### Experiments Folder

- `experimental_comparison.py`: Compares different types of selection, crossover and mutation methods.
- `experimental_comparison_CI.py`: Compares different configurations and parameters of the GA, adding the Confidence Intervals.
- `penalties_comparison.py`: Compares different hard and soft contraints penalties.

### GeneticAlgorithmComponents Folder

- `crossover.py`: Defines the crossover methods of our GA.
- `genetic_algorithm.py`: The genetic algorithm script to implement the genetic operators.
- `mutation.py`: Defines the mutation methods in GA.
- `selection.py`: Defines the selection methods of our GA.

### Utils Folder

- `constants.py`: Contains constants used throughout the project (e.g. population size, hard and soft constraints penalties).
- `display.py`: Defines the visualizations to display the schedules.

### Other Files

- `data.py`: Manages the input data required for scheduling.
- `main.py`: The main file for running the scheduling algorithm.
- `README.md`: This README file.
- `PasteisDeData.pdf`: Detailed project report.

## Usage

Adjust the parameters and configurations in the respective Python scripts to fine-tune the Genetic Algorithm's performance. Use the pyhton files on the `Experiments` folder to compare different configurations.


Happy Scheduling!
