# Unitests and Integration tests
Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

### Common Testing Patterns

#### Mocking

- **Purpose:** Mocking involves creating objects that simulate the behavior of real objects. It's used to isolate the code being tested and avoid dependencies on external systems.
- **Usage:** Mocking libraries or tools provide the ability to create mock objects or functions that mimic the behavior of real components. This allows developers to test code without relying on the complete functionality of external dependencies.
- **Example:** In unit testing, a database connection might be replaced with a mock object to simulate database interactions without actually connecting to a database.

#### Parametrization

- **Purpose:** Parametrization allows testing a piece of code with multiple inputs or scenarios.
- **Usage:** Using parameterized tests, you can define a test method once and run it with different sets of inputs or configurations.
- **Example:** Testing a sorting algorithm with different types of input data (empty list, already sorted list, random list) by providing various inputs and expected outcomes.

#### Fixtures

- **Purpose:** Fixtures are used to set up and provide a baseline for tests by providing the necessary context or environment.
- **Usage:** They can initialize resources, create test data, or configure the testing environment before test execution. They help ensure that tests run consistently and reliably.
- **Example:** Setting up a database connection, creating temporary files, or initializing objects required for testing.
