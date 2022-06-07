# Unit testing
-   I wrote 5 test cases
-   To run the tests, we use the following command: 
```bash
   coverage run -m unittest ".\tests\unit-tests\test_app.py"
```
![unit test](https://user-images.githubusercontent.com/62619786/172247151-ab98ff82-f117-4a0a-9559-c16a46a9d1f9.PNG)


# Integration testing
-   I wrote 6 test cases for 4 routes of the application.
-   To run the tests, we use the following command: 
```bash
  coverage run -m pytest ".\tests\integration-tests\test_integration_app.py"
```
Running these tests have provided the following results:
![integration](https://user-images.githubusercontent.com/62619786/172247135-f4b86c78-9058-4cc1-9235-1063fa0b2df3.png)

```bash
   coverage report
```
![coverage](https://user-images.githubusercontent.com/62619786/172408664-65991a71-3cdc-445c-bde4-97fbb191ed72.PNG)

# E2E testing
-   I wrote 3 e2e test cases for 3 different functionnalities of the application. I used selenium to navigate through the web pages
-   To run the tests, we use the following command:
```bash
   coverage run -m pytest .\tests\e2e-tests\test_e2e_app.py
```
![e2e](https://user-images.githubusercontent.com/62619786/172411408-8fa192d3-b845-4658-9f8a-b8253f418dfe.PNG)

# UAT
