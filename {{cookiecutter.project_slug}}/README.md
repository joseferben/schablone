# {{cookiecutter.project_slug}}

Just a simple {{cookiecutter.project_slug}}

## Running locally

    $ python -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements/dev.txt
    $ make init
    $ make data
    $ make dev

## Deployment

1. Create a AWS IAM user `{{cookiecutter.project_slug}}` with following policy attached:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetBucketLocation", "s3:ListBucket"],
      "Resource": "arn:aws:s3:::{{cookiecutter.project_slug}}"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:DeleteObject", "s3:GetObject"],
      "Resource": [
        "arn:aws:s3:::{{cookiecutter.project_slug}}/*",
        "arn:aws:s3:::{{cookiecutter.project_slug}}"
      ]
    }
  ]
}
```

2. Prepare the secrets:

`$ cp .env.sample .env`

Use `openssl rand -base64 32` to create a Django secret.

3. Launch!

```sh
    $ fly launch
    $ fly secrets import < .env
    $ fly volumes create data -s 1
    $ fly scale memory 512
    $ fly deploy
```

4. Setup Github Actions

`$ fly auth token`

And create a secret `FLY_API_TOKEN` in the Github repo.
