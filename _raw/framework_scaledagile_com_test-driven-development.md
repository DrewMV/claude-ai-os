---
source_url: https://framework.scaledagile.com/test-driven-development
scraped: 2026-05-30
authenticated: true
---

SAFe Knowledge Base » Test-Driven Development

Test-Driven Development

We never have enough time for testing, so let's just write the test first.

—Kent Beck

Test-Driven Development (TDD) is a philosophy and practice that involves building and executing tests before implementing the code or a system component. By validating them against a series of agreed-to tests, TDD—an Agile Testing practice—improves system outcomes by ensuring the system implementation meets its requirements. TDD and Behavior-Driven Development (BDD) are part of the 'test-first' approach to achieving Built-in Quality. Writing tests first creates a more balanced testing approach with many fast, automated development tests and fewer slow, manual, end-to-end tests. (See the Built-in Quality section of the Team and Technical Agility article for more detail on the testing pyramid and a balanced testing portfolio.)

Details

Kent Beck and others have defined a set of Extreme Programming (XP) practices under the umbrella label of TDD [1]. Figure 1 illustrates the process:

Figure 1. The Test-Driven Development process

Write the test first, ensuring that the developer understands the required behavior. This could be a new test or a modification of an existing test.
Run the test and watch it fail. Because there's no code yet, this may seem pointless. Still, it accomplishes two practical objectives: it verifies the test works, including any testing harnesses, and demonstrates how the system will behave if the code is incorrect.
Write the minimum amount of code needed to pass the test. If it fails, rework the code or the test until it passes routinely.
Continue implementing new code until all tests pass. This step gives the developer confidence that their changes meet the current requirements and haven't created an error in another part of the system.
Refactor as necessary to ensure the design aligns with changing requirements (for example, emergent design). Developers continually update their designs to ensure that evolving requirements and a growing codebase don't lead to poor code quality.

In XP, this practice was designed primarily to operate in the context of unit tests, developer-written tests (also a form of code) that evaluate the classes and methods used. These are a form of 'white-box testing' because they test the internals of the system and the various code paths. To help assure high quality, developers work in pairs to create the code and tests, providing multiple perspectives and a built-in peer review. Even when not developed in pairs, the tests give another set of eyes that review the code.

A rich set of unit tests ensure that refactoring efforts do not introduce new errors, allowing developers to improve their designs continuously. Refactoring builds quality in by enabling designs to emerge over time, supporting the solution's changing requirements.

Unit Tests

TDD creates a large set of developer-level tests, which allows Quality Assurance (QA) and test personnel to focus on other testing challenges. Instead of spending time finding and reporting code-level bugs, they can focus on more complex behaviors and interactions between components.

The open-source community has built unit testing frameworks to cover most languages, including Java, C, C#, C++, XML, HTTP, Python, and others. There are unit-testing frameworks for most coding environments a developer is likely to encounter. Unit testing frameworks provide a harness for the development and maintenance of unit tests and for automatically executing them against the system.

With TDD, testing, and code are written together and occur within the same Iteration. As a result, the regression test automation for unit tests is mostly free for the team. Unit testing is a cornerstone of software agility. Investing in comprehensive unit testing improves quality and productivity.

Component Tests

Teams also use tests to evaluate larger-scale components of the system. Many of these are in various architectural layers, providing services needed by Features or other modules. Testing tools and practices for implementing component tests vary. For example, testing frameworks can hold complicated unit tests written in the development language (for example, Java, C, C#, and so on). This allows many teams to build component tests using their unit testing frameworks. They may not even consider their separate functions, as it's merely part of their testing strategy. In other cases, developers may incorporate other testing tools or write entirely customized tests in any language or environment that is productive for them to test broader system behaviors. These tests are also automated to defend against unanticipated consequences of refactoring and new code.

Speeding Up Testing with Test Doubles

TDD tests exercise a relatively small part of the system, yet, each test can require significant time and expense to launch and set up. Also, each may require dependent components and enterprise infrastructure that may or may not be available immediately. 'Test doubles' are code constructs that accelerate testing by substituting slow, unavailable, or expensive components with faster proxies. TDD practices typically make significant use of test doubles. See the Built-in Quality article for more background and application information on test doubles.

Learn More

[1] Beck, Kent. Test-Driven Development. Addison-Wesley, 2003.

Last update: 23 February 2023
