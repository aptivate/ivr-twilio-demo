from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import View

from twilio import twiml
from django_twilio.decorators import twilio_view


@twilio_view
def say_words(request, words="Goodbye"):
    r = twiml.Response()
    r.say(words)
    return r


@twilio_view
def gather(
    request, words="Press 1 to hang up.",
    handler_url_name='process_demo',
    timeout=10, numDigits=1,
):
    r = twiml.Response()
    action = reverse(handler_url_name)
    with r.gather(numDigits=numDigits, timeout=timeout, action=action, method='POST') as g:  # nopep8
        g.say(words)
    return r


@twilio_view
def process_demo(request):
    phrases = {
        '1': 'Goodbye',
        '2': 'Hello monkey',
    }
    digit = request.POST.get('Digits', '1')
    if digit != '2':
        digit = '1'
    return say_words(request, words=phrases[digit])


class LoopWithGather(View):
    """
    Demonstrates a CBV looping and gathering a single digit.
    When a single digit is pressed, the looping will begin again (the view
    is re-called).
    """

    @method_decorator(twilio_view)
    def dispatch(self, request, *args, **kwargs):
        return super(LoopWithGather, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        r = twiml.Response()
        with r.gather(numDigits=1) as g:
            g.say(
                text="Hello, monkey. Classy!",
                voice='woman',
                language='en-gb',
                loop=5
            )
        return r
