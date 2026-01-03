
```python
if __name__ == "__main__":
    e = ""

    assert len(e) == 0
    if not e:
        assert True

    s = "hello"

    # strings are immutable!
    # TypeError: 'str' object does not support item assignment
    try:
        s[1] = 'a'
        assert False
    except Exception:
        ...


    # Convoluted, eh?
    s = s[:1] + 'a' + s[2:]
    assert s == "hallo"

    assert "hello" + "world" == "helloworld"

    i = 1
    assert f'{i}' == '1'
    assert f'{i=}' == 'i=1'

    name = 'john'
    assert 'hello %s' % (name) == 'hello john'
    assert 'hello {}'.format(name) == 'hello john'
    assert f'hello {name}' == 'hello john'
    # f-strings are modern and preferred!

    assert 'j' in 'john'
    assert 'j' == 'j'
    assert 'jo' <= 'john'
    assert 'jo' in 'john'
    assert 'jn' not in 'john'
    assert 'jn' <= 'john' # set-in
    assert 'john' <= 'john' # set-in
    assert hash('j') == hash('j')
    assert hash('j') != hash('o')

    assert 'a' * 3 == 'aaa'
    assert 3 * 'a' == 'aaa'

    assert str('3') == '3'
    assert repr('3') == "'3'"

    assert 'john'.capitalize() == 'John'
    assert 'JoHn'.casefold() == 'john'
    assert 'john'.center(10) == '   john   '
    assert 'john'.center(10, '-') == '---john---'

    assert 'john'.count('o') == 1

    assert 'john'.endswith('hn')
    assert 'john'.startswith('jo')
    assert 'john'.startswith('j')
    assert 'john'.find('j') == 0
    assert 'john'.find('k') == -1
    assert 'jono'.find('o') == 1
    try:
        assert 'john'.index('k') == -1
        assert False
    except Exception:
        ...

    assert 'a'.isalpha()
    assert 'aw'.isalpha()
    assert '12'.isdigit()
    assert 'a'.isalnum()

    def myisalpha(c):
        ## assert 'a' <= c <= 'z' or 'A' <= c <= 'Z'
        assert 'a' <= c.lower() <= 'z'

    def myisdigit(c):
        assert 0 <= c.lower() <= 9

    def myisdigit2(s):
        assert isinstance(s, str)
        for c in s:
            assert 0 <= c.lower() <= 9

    assert ''.join(["1","2","3"]) == '123'
    assert ','.join(["1","2","3"]) == '1,2,3'
    assert ''.join(str(n) for n in [1,2,3]) == '123'

    assert " foo ".strip() == "foo"
    assert " foo ".lstrip() == "foo "
    assert " foo ".rstrip() == " foo"

    assert "HI".lower() == 'hi'
    assert "hi".upper() == 'HI'

    assert "foo,bar".partition(',') == ('foo', ',', 'bar')
    assert "foobar".partition(',') == ('foobar', '', '')

    assert "foo,bar".split(',') == ['foo', 'bar']
    assert "foo bar".split() == ['foo', 'bar']
    assert "foo bar".split(' ') == ['foo', 'bar']
    assert "foo  bar".split('  ') == ['foo', 'bar']


    assert 'hello world'.removeprefix('hello ') == 'world'
    assert 'hello world'.removesuffix(' world') == 'hello'

    assert 'hello world'.replace('hello', 'bye') == 'bye world'
    assert 'hello world hello'.replace('hello', 'bye', 1) == 'bye world hello'
    assert 'hello world hello'.replace('hello', 'bye', 2) == 'bye world bye'
    assert 'hello world hello'.replace('hello', 'bye', -1) == 'bye world bye'

    assert 'ha'.translate({
        'h': 't',
        'a': 'o',
    }) == 'ha'
```

