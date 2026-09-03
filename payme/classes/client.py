import typing as t

from payme.const import Networks

from payme.classes.cards import Cards
from payme.classes.receipts import Receipts
from payme.classes.initializer import Initializer
from payme.types.response import cards as card_response
from payme.types.response import receipts as receipt_response


class Payme:
    """
    The payme class provides a simple interface
    """

    def __init__(
        self,
        payme_id: str,
        payme_key: t.Optional[str] = None,
        is_test_mode: bool = False,
        fallback_id: t.Optional[str] = None,
        *args,
        **kwargs,
    ) -> None:
        url = Networks.PROD_NET.value

        if is_test_mode is True:
            url = Networks.TEST_NET.value

        self.cards = Cards(url=url, payme_id=payme_id)
        self.initializer = Initializer(
            payme_id=payme_id, fallback_id=fallback_id, is_test_mode=is_test_mode
        )
        if payme_key:
            self.receipts = Receipts(url=url, payme_id=payme_id, payme_key=payme_key)

    def cards_create(
        self,
        number: str,
        expire: str,
        save: bool = False,
        timeout: int = 10
    ) -> card_response.CardsCreateResponse:
        """
        Create a new card.

        :param number: The card number.
        :param expire: The expiration date of the card in MMYY format.
        :param save: A boolean indicating whether to save the card for future
            use (default is False).
        :param timeout: The request timeout duration in seconds (default is
            10 seconds).
        :return: A CardsCreateResponse object containing the response data.
        """
        return self.cards.create(number=number, expire=expire, save=save, timeout=timeout)

    def cards_get_verify_code(
        self,
        token: str,
        timeout: int = 10
    ) -> card_response.GetVerifyResponse:
        """
        Retrieve a verification code for a specified token.

        :param token: The token associated with the card.
        :param timeout: The request timeout duration in seconds (default is
            10 seconds).
        :return: A GetVerifyResponse object containing the response data.
        """
        return self.cards.get_verify_code(token=token, timeout=timeout)

    def cards_verify(
        self,
        token: str,
        code: str,
        timeout: int = 10
    ) -> card_response.VerifyResponse:
        """
        Verify a verification code for a specified token.

        :param token: The token associated with the card.
        :param code: The verification code to be verified.
        :param timeout: The request timeout duration in seconds (default is
            10 seconds).
        :return: A VerifyResponse object containing the response data.
        """
        return self.cards.verify(token=token, code=code, timeout=timeout)

    def cards_remove(
        self,
        token: str,
        timeout: int = 10
    ) -> card_response.RemoveResponse:
        """
        Remove a card from the Paycom system.

        :param token: The token associated with the card.
        :param timeout: The request timeout duration in seconds (default is
            10 seconds).
        :return: A RemoveResponse object containing the response data.
        """
        return self.cards.remove(token=token, timeout=timeout)

    def cards_check(
        self,
        token: str,
        timeout: int = 10
    ) -> card_response.CheckResponse:
        """
        Check the status of a card.

        :param token: The token associated with the card.
        :param timeout: The request timeout duration in seconds (default is
            10 seconds).
        :return: A CheckResponse object containing the response data.
        """
        return self.cards.check(token=token, timeout=timeout)

    def cards_test(self) -> None:
        """
        Run a comprehensive test suite for card functionalities including
        creation, verification, status check, and removal.
        """
        return self.cards.test()

    def receipts_create(
        self,
        account: dict,
        amount: t.Union[float, int],
        description: t.Optional[str] = None,
        detail: t.Optional[t.Dict] = None,
        timeout: int = 10,
    ) -> receipt_response.CreateResponse:
        """
        Create a new receipt.

        :param account: The account details for the receipt.
        :param amount: The amount of the receipt.
        :param description: Optional description for the receipt.
        :param detail: Optional additional details for the receipt.
        :param timeout: The request timeout duration in seconds (default 10).
        """
        return self.receipts.create(
            account=account,
            amount=amount,
            description=description,
            detail=detail,
            timeout=timeout
        )

    def receipts_pay(
        self,
        receipts_id: str,
        token: str,
        timeout: int = 10
    ) -> receipt_response.PayResponse:
        """
        Pay the receipt using a token.

        :param receipts_id: The ID of the receipt used for payment.
        :param token: The token associated with the card.
        :param timeout: The request timeout duration in seconds (default is 10).
        """
        return self.receipts.pay(receipts_id=receipts_id, token=token, timeout=timeout)

    def receipts_send(
        self,
        receipts_id: str,
        phone: str,
        timeout: int = 10
    ) -> receipt_response.SendResponse:
        """
        Send the receipt to a mobile phone.

        :param receipts_id: The ID of the receipt used for payment.
        :param phone: The phone number to send the receipt to.
        :param timeout: The request timeout duration in seconds (default 10).
        """
        return self.receipts.send(receipts_id=receipts_id, phone=phone, timeout=timeout)

    def receipts_cancel(
        self,
        receipts_id: str,
        timeout: int = 10
    ) -> receipt_response.CancelResponse:
        """
        Cancel the receipt.

        :param receipts_id: The ID of the receipt used for payment.
        :param timeout: The request timeout duration in seconds (default 10).
        """
        return self.receipts.cancel(receipts_id=receipts_id, timeout=timeout)

    def receipts_check(
        self,
        receipts_id: str,
        timeout: int = 10
    ) -> receipt_response.CheckResponse:
        """
        Check the status of a receipt.

        :param receipts_id: The ID of the receipt used for payment.
        :param timeout: The request timeout duration in seconds (default 10).
        """
        return self.receipts.check(receipts_id=receipts_id, timeout=timeout)

    def receipts_get(
        self,
        receipts_id: str,
        timeout: int = 10
    ) -> receipt_response.GetResponse:
        """
        Get the details of a specific receipt.

        :param receipts_id: The ID of the receipt used for payment.
        :param timeout: The request timeout duration in seconds (default 10).
        """
        return self.receipts.get(receipts_id=receipts_id, timeout=timeout)

    def receipts_get_all(
        self,
        count: int,
        from_: int,
        to: int,
        offset: int,
        timeout: int = 10
    ) -> receipt_response.GetAllResponse:
        """
        Get all receipts for a specific account.

        :param count: The number of receipts to retrieve.
        :param from_: The start index of the receipts to retrieve.
        :param to: The end index of the receipts to retrieve.
        :param offset: The offset for pagination.
        :param timeout: The request timeout duration in seconds (default 10).
        """
        return self.receipts.get_all(
            count=count,
            from_=from_,
            to=to,
            offset=offset,
            timeout=timeout
        )

    def receipts_set_fiscal_data(
        self,
        receipt_id: str,
        qr_code_url: str,
        timeout: int = 10
    ) -> receipt_response.SetFiscalDataResponse:
        """
        Set fiscal data for a receipt.

        :param receipt_id: The ID of the receipt used for payment.
        :param qr_code_url: URL of the fiscal check from the ofd.uz.
        :param timeout: The request timeout duration in seconds (default 10).
        """
        return self.receipts.set_fiscal_data(
            receipt_id=receipt_id,
            qr_code_url=qr_code_url,
            timeout=timeout
        )

    def receipts_test(self) -> None:
        """
        Run a comprehensive test suite for receipts functionalities.
        """
        if not hasattr(self, 'receipts'):
            raise AttributeError("Receipts not initialized. Provide payme_key in constructor.")
        return self.receipts.test()

    def generate_pay_link(
        self,
        id: int,
        amount: int,
        return_url: str
    ) -> str:
        """
        Generate a payment link for a specific order.

        This method encodes the payment parameters into a base64 string and
        constructs a URL for the Payme checkout.

        :param id: Unique identifier for the account.
        :param amount: The amount associated with the order in currency units.
        :param return_url: The URL to which the user will be redirected after
            the payment is processed.
        :return: A payment link formatted as a URL, ready to be used in the
            payment process.
        """
        return self.initializer.generate_pay_link(
            id=id,
            amount=amount,
            return_url=return_url
        )

    def generate_fallback_link(
        self,
        form_fields: dict = None
    ) -> str:
        """
        Generate a fallback URL for the Payme checkout.

        :param form_fields: Additional query parameters to be appended to the
            fallback URL.
        :return: A fallback URL formatted as a URL, ready to be used in the
            payment process.
        """
        return self.initializer.generate_fallback_link(form_fields=form_fields)
