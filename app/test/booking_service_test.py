import unittest

from models import booking_item, booking
from repositories.in_memory_booking_repository import InMemoryBookingRepository
from services import booking_service


class BookingServiceTest(unittest.TestCase):

    def test_that_users_create_booking(self):
        booking_item_one : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "7477sfsfouhugslerugsorygikfgkvs",
            quantity= 1,
            total_amount= 1000.00
        )

        booking_item_two : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "hsruputhgwoeuhgwpodumeje",
            quantity= 1,
            total_amount= 1900.00
        )

        bookings = booking.Booking.CreateBooking(
            user_id= "ddhdh",
            event_id= "uueue",
            ticket_type= "Vip",
            bookings= [booking_item_one, booking_item_two],
            quantity= 1,
            total_amount= 2900.00,
        )
        service = booking_service.BookingService(InMemoryBookingRepository())
        response : booking.CreateBookingResponse = service.add_booking(bookings)
        self.assertEqual(2900.00, response.total_amount)




    def test_that_users_create_booking_with_correct_userId(self):
        booking_item_one : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "7477sfsfouhugslgsorygikfgkvs",
            quantity= 1,
            total_amount= 1000.00
        )

        booking_item_two : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "hsruputhgwogwpodumeje",
            quantity= 1,
            total_amount= 1900.00
        )

        bookings = booking.Booking.CreateBooking(
            user_id= "ddh",
            event_id= "uue",
            ticket_type= "Vip",
            bookings= [booking_item_one, booking_item_two],
            quantity= 1,
            total_amount= 2900.00,
        )
        service = booking_service.BookingService(InMemoryBookingRepository())
        response : booking.CreateBookingResponse = service.add_booking(bookings)
        self.assertEqual("ddh", response.user_id)



    def test_that_users_create_booking_then_update_credentials(self):
        booking_item_one : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "7477sfsfouhslgsorygikfgkvs",
            quantity= 1,
            total_amount= 1000.00
        )

        booking_item_two : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "hsruputogwpodumeje",
            quantity= 1,
            total_amount= 1900.00
        )

        bookings = booking.Booking.CreateBooking(
            user_id= "ddh",
            event_id= "uue",
            ticket_type= "Vip",
            bookings= [booking_item_one, booking_item_two],
            quantity= 1,
            total_amount= 2900.00,
        )
        service = booking_service.BookingService(InMemoryBookingRepository())
        response : booking.CreateBookingResponse = service.add_booking(bookings)
        self.assertEqual("ddh", response.user_id)



        booking_item_one : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "7477sfsfouhslgsorygikfgkvs",
            quantity= 1,
            total_amount= 100.00
        )

        booking_item_two : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "hsruputogwpodumeje",
            quantity= 1,
            total_amount= 100.00
        )

        update_bookings = booking.Booking.UpdateBooking(
            id=response.id,
            user_id="ddh",
            event_id="uue",
            ticket_type="Vip",
            bookings=[booking_item_one, booking_item_two],
            quantity=1,
            total_amount=200.00,
        )

        response : booking.UpdateBookingResponse = service.update_booking(update_bookings)
        self.assertEqual(200.00, response.total_amount)


    def test_that_users_create_booking_user_delete_booking(self):
        booking_item_one : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "7477uhugslerugsorygikfgkvs",
            quantity= 1,
            total_amount= 1000.00
        )

        booking_item_two : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "hsrupgwoeuhgwpodumeje",
            quantity= 1,
            total_amount= 1900.00
        )

        bookings = booking.Booking.CreateBooking(
            user_id= "ddhdh",
            event_id= "uueue",
            ticket_type= "Vip",
            bookings= [booking_item_one, booking_item_two],
            quantity= 1,
            total_amount= 2900.00,
        )
        service = booking_service.BookingService(InMemoryBookingRepository())
        response : booking.CreateBookingResponse = service.add_booking(bookings)
        self.assertEqual(2900.00, response.total_amount)

        delete_booking = booking.Booking.DeleteBooking(
            id=response.id
        )

        syst_response : booking.Booking.DeleteBookingResponse = service.delete_booking(delete_booking)

        self.assertEqual("Booking deleted", syst_response.message)


    def test_that_users_create_booking_user_get_booking_information(self):
        booking_item_one : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "7477uhugslerugsorygikfgkvs",
            quantity= 1,
            total_amount= 1000.00
        )

        booking_item_two : booking_item.BookingItem = booking_item.BookingItem(
            ticket_type_id= "hsrupgwoeuhgwpodumeje",
            quantity= 1,
            total_amount= 1900.00
        )

        bookings = booking.Booking.CreateBooking(
            user_id= "ddhdh",
            event_id= "uueue",
            ticket_type= "Vip",
            bookings= [booking_item_one, booking_item_two],
            quantity= 1,
            total_amount= 2900.00,
        )
        service = booking_service.BookingService(InMemoryBookingRepository())
        response : booking.CreateBookingResponse = service.add_booking(bookings)
        self.assertEqual(2900.00, response.total_amount)

        booking_info = booking.Booking.GetBookingInformation(
            id=response.id
        )

        info : booking.Booking.GetBookingInformationResponse = service.get_booking_information(booking_info)

        self.assertEqual(2900.00, info.total_amount)