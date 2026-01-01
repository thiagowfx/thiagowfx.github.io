
I needed to translate the following shell command (`bash`):

```shell
instance="thiago-perrotta"
kubectl get secret -n "c-$instance" "$instance-factory" -o jsonpath='{.data.conf\.json}' | base64 --decode | jq --arg url 'rabbitmq.url' -r '.[$url]'
```

...to Ruby. It reads a JSON entry from a kubernetes secret and extracts a
specific key from it with `jq`.

I wrote a helper function to do so:

```ruby
def factory_conf_json_rabbitmq_url
  # amqp://{user}:{password}@{host}:{port}
  Helpers::LocalShell.capture_without_error(
    "kubectl get secret -n c-#{@target.name} #{@target.name}-factory -o jsonpath='{.data.conf\.json}' | base64 --decode | jq --arg url 'rabbitmq.url' -r '.[$url]'"
  )&.strip&.split('@')&.last&.split(':')&.first
end
```

It took me a long time to figure out what was wrong with that code. It was
returning an empty string.

It turns out it was a very simple issue: string escaping!

One must do `{.data.conf\\.json}`. The backslash needs to be escaped.

How did I figure it out? Heck, I didn't. I just asked ChatGPT how to translate
the shell expression above into Ruby, and it has correctly emitted the escaped
string in Ruby.

In hindsight, the error is quite obvious. Isn't it always like that?[^1].

[^1]: I feel I should incorporate more AI in my daily dev workflows. However, I
    want to do so efficiently. Paying for Claude / ChatGPT doesn't make sense to
    my use case as there's no unlimited usage (yet?), and I don't want to stress
    over "wasting" prompts. It's not a good user experience to worry about
    getting close to the limit. It's like when doing web searches: you don't
    stress over them because you know you can make new queries as many times as
    you would like. So far I use only discrete chat conversations + Github
    Copilot in VSCode.

