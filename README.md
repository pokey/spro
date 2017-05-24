Spro
====

Use [SigOpt](https://sigopt.com/) to tune espresso brewing parameters.

Installation
------------
Run

```
pip install -e .
```

This has only been tested with Python 3, so if you're not using pyenv and
you're on a Mac, you might want to

```
brew install python3
```

and then replace `pip` with `pip3` in the above step.  Ie

```
pip3 install -e .
```

Running
-------
1. Sign up for [SigOpt](https://sigopt.com/).  Copy your API token.
1. Create a new experiment.  You'll run this step for each new bag of coffee
   you buy:

   ```
   SIGOPT_API_TOKEN=xxx spro create foo
   ```

   Using your API token from sigopt.  This will create an experiment called
   "foo".  You can call it whatever you want; maybe name it based on the bag of
   coffee you're using.  Make a note of the experiment id, as you'll use this
   in the next step.
1. Run the optimization loop:

   ```
   SIGOPT_API_TOKEN=xxx spro optimize 1234
   ```

   replacing `1234` with the experiment id from the previous step.  Brew shots
   using the given parameters as instructed.  You can exit with `Ctrl-C`, and
   when you run `optimize` again it will pick up where you left off.  Go back
   to the previous step when you get a new bag of coffee.

Credits
-------
This repo was created with
[cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
