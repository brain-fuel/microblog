# Microblog Project

## Dev Hints

### Virtual Environment

In order to activate virtual environment for macos and linux, from the bash shell run:

```bash
source ./venv/bin/activate
```

To exit virtual environment, run:

```bash
deactivate
```

### See Project Structure

In order to see the project structure without all the extraneous virtual environment stuff and \_\_pycache\_\_ folder:

```bash
tree -I '__pycache__|venv'
```

If you wish to alias this as `pytree`, you can run:

```bash
alias pytree="tree -I '__pycache__|venv'"
```

If you don't want to have to run the alias command every time, you can echo this to your .bashrc file:

```bash
echo "alias pytree=\"tree -I '__pycache__|venv'\"" >> ~/.bashrc
```
