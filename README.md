# API-tests-on-GamerPower-in-parallel-and-UI-tests-on-YouTube

This project is a testing framework for the GamerPower API, designed to verify its functionality and performance under various conditions.

## Project Structure

The project consists of three main modules:

1. **infra**: Contains infrastructure-related code, including API wrappers and browser wrappers.
   - `api_wrapper.py`: Defines the `GamerPowerAPI` class for interacting with the GamerPower API.
   - `browser_wrapper.py`: Provides a wrapper for browser-related operations.

2. **logic**: Contains the business logic of the testing framework.
   - `api_logic.py`: Implements the `GamerPower` class, which extends the `GamerPowerAPI` class and includes methods for testing different functionalities of the GamerPower API.

3. **test**: Includes unit tests for the GamerPower API.
   - `api_test.py`: Defines unit test cases for various functionalities of the `GamerPower` class.
   - `test_runner.py`: Executes the unit tests either serially or in parallel based on configuration.

## Running the Tests

To run the tests, follow these steps:

1. Install the required dependencies by running:
