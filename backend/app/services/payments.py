from app.services.base import CrudService


class PaymentService(CrudService):
    collection = "payments"


payment_service = PaymentService()
