# PassGen

A simple password generator command line interface.

## Stories

- [x] As a user I want to generate a random secure password to protect my personal accounts
    - [x] Minimal length
    - [x] Include symbols
    - [x] Include numbers
- [x] As a user I want the generated password to be copied to the clipboard
- [x] As a user I want the generated password to be saved to a file


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installing

Clone the project repository

```shell
git clone https://github.com/rjNemo/pass-gen
```

Install dependencies

```shell
pipenv install
```

Run it using:

```shell
make cli
```

Find more information about available commands running

```shell
make help
```

## Running the tests

```shell
make test
```


## Built With

- [Typer](https://typer.tiangolo.com/) - Typer, build great CLIs. Easy to code. Based on Python type hints

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/rjNemo/pass-gen/tags).

## Authors

- **Ruidy** - _Initial work_ - [Ruidy](https://github.com/rjNemo)

See also the list of [contributors](https://github.com/rjNemo/pass-gen/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

