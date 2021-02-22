from bbquote.lib import get_quote

def test_get_quote():
  assert "-" in get_quote().split()