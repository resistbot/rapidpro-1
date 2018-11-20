
from django.utils.translation import ugettext_lazy as _

from temba.contacts.models import ZENDESK_SCHEME

from ...models import ChannelType
from .views import ClaimView


class ZendeskType(ChannelType):
    """
    An Zendesk channel
    """

    code = "ZD"
    category = ChannelType.Category.API

    courier_url = r"^abc/(?P<uuid>[a-z0-9\-]+)/receive$"



    name = "Zendesk"
    icon = "icon-fcm"

    claim_blurb = _(
        """Connect your approved <a href="https://www.zendesk.com/" target="_blank">Zendesk</a> app"""
    )
    claim_view = ClaimView

    schemes = [ZENDESK_SCHEME]
    attachment_support = True
    free_sending = True

    configuration_blurb = _(
        """
        To use your Zendesk channel you'll have to configure the Zendesk server to direct messages to the url below.
        """
    )

    configuration_urls = (
        dict(
            label=_("Receive URL"),
            url="https://{{ channel.callback_domain }}{% url 'courier.abc' channel.uuid %}",
            description=_(
                "POST Zendesk trigger to this address."
            ),
        ),
    )
