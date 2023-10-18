# Using Github Actions to Automatically Lint and Unit Test Commits to Repository

## Changelog

The periodic time calculation algorithm is largely unchanged. The one exception is that instead of using a lambda function,
```Python
calculate_periodic_time= (lambda l: 2* math.pi/ math.sqrt(g / l))
return calculate_periodic_time
```
The calculation is simply contained in the return statement
return 2 * math.pi * math.sqrt(l / g)
To make the module more compact.

## Action Implementation
### Linting

The linting action is implemented in the file final_lint.yml. Generally speaking, it will automatically lint every file that is pused to the main branch of the repository. Here's how it works:


We start by defining the trigger. This means that this action will run whenever there is a push to the main branch of the repo
``` YAML
on:
  push:
    branches:
      - main
```

Now we run some initialization steps. We run the action on ubuntu with python version 3.8. We also need to checkout the code for it to be linted on this machine.
```YAML
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.8
```

We now need to install all necessary dependencies. We first make sure to install the latest version of pip, the python package manager. This will allow us to install pylint.
```YAML
name: Install dependencies
      
      run:
        python -m pip install --upgrade pip
```

We then install pylint
```YAML
name: Install linter
      run:
        pip install pylint
```

We finally lint the pushed code via
```YAML
name: lint final_code.py
      run: pylint final_code.py || exit 0
```

### Unit Testing

For the unit test, we follow the same steps in the unit.yml file until we install the necessary dependencies. We now need to install pytest with 
```YAML
pip install pytest
```
And we then unittest the file pushed with
```YAML
pytest unit.py
```
