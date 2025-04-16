# Taller de automatización de pruebas con Selenium, Python, Cucumber, Gherkin, y el patrón Page Object Model (POM).

# Paso 1: Instalación de Herramientas

## Antes de iniciar, asegúrate de tener instaladas las siguientes herramientas:
	- Python (https://www.python.org/downloads/) 
	- Selenium (pip install selenium)
	- Behave para Cucumber con Python (pip install behave)
	- Cucumber para casos de prueba con Gherkin (Esto ya viene con Behave.)

## Para correr los tests, usa el comando:
	- behave (debes correrlo en la terminal o consola de comandos desde la raíz de tu proyecto.)


---


# Automated Testing Project with Selenium and GitHub Actions

## ✨ Overview

This project includes a set of automated tests to validate critical functionalities of a web application, such as user login and purchase flow. It uses tools like **Selenium**, **Behave (BDD)**, and **GitHub Actions** for continuous test execution.

---

## 💡 Workflow

### 1. Test Creation:

- **Page files** were implemented following the Page Object Model pattern.
- **Steps** and `.feature` files were developed to:
  - Test user **login**.
  - Validate a complete **purchase flow**.
- All tests passed successfully at the local level.

### 2. Attempt with Azure Pipelines:

- CI was initially attempted using **Azure DevOps Pipelines**.
- However, **additional free minutes** were needed.
- The support response took **up to 2 days**, so the decision was made to **switch platforms**.

### 3. Migration to GitHub Actions:

- A **GitHub Actions workflow** was configured to run the tests.
- When using Linux runners, errors arose related to Chrome running in headless environments.

### 4. Bug Fixes:

- The `environment.py` file was modified to include execution options like:
  - `--headless`
  - `--no-sandbox`
  - `--disable-dev-shm-usage`
- Browser shutdown handling was improved to avoid errors when the driver isn't initialized.

### 5. Final Result:

- The GitHub Actions pipeline **successfully runs** all tests on each push.
- The testing system is fully automated and functional.

---

## <b> Autora </b>

+ [Gloria Vanesa](https://github.com/Vanesa155 "Vanesa V.")

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
