

from smartmin.views import SmartFormView

from django import forms
from django.utils.translation import ugettext_lazy as _

from ...models import Channel
from ...views import ClaimViewMixin


class ClaimView(ClaimViewMixin, SmartFormView):
    class Form(ClaimViewMixin.Form):
        title = forms.CharField(required=True, label=_("Zendesk Environment Title"), help_text=_("The name of your environment"))

        base_url = forms.CharField(
            required=True,
            label=_("Zendesk Base URL / Subdomain"),
            help_text=_("Your zendesk subdomain https://mycompany.zendesk.com"),
        )
        username = forms.CharField(
            required=True, label=_("Zendesk Account Username"), help_text=_("The API user's email address.")
        )
        auth_token = forms.CharField(
            required=True, label=_("Zendesk API Auth Token"), help_text=_("The API auth token.")
        )

    form_class = Form

    def form_valid(self, form):
        org = self.request.user.get_org()

        title = form.cleaned_data.get("title")
        username = form.cleaned_data.get("username")
        auth_token = form.cleaned_data.get("auth_token")
        base_url = form.cleaned_data.get("base_url")
        config = {
            Channel.CONFIG_USERNAME: username,
            Channel.CONFIG_AUTH_TOKEN: auth_token,
            Channel.CONFIG_BASE_URL: base_url,
        }

        self.object = Channel.create(
            org, self.request.user, None, self.channel_type, name=title, config=config
        )

        return super().form_valid(form)
