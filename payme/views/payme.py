from payme.views.base import BasePaymeWebHookAPIView


class PaymeWebHookAPIView(BasePaymeWebHookAPIView):
    """
    A webhook view for Payme with callback handlers.
    """

    def handle_pre_payment(self, params, result, *args, **kwargs):
        """
        Handle the pre_create_transaction action. You can override this method
        """
        print(f"Transaction pre_created for this params: {params} and pre_created_result: {result}")

    def handle_created_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction created for this params: {params} and cr_result: {result}")

    def handle_successfully_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction successfully performed for this params: {params} and performed_result: {result}")

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        """
        Handle the cancelled payment. You can override this method
        """
        print(f"Transaction cancelled for this params: {params} and cancelled_result: {result}")
