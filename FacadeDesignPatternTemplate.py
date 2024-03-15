class VenueBooking:
    """
    creating a subsystem responsible for Booking venue 
    """
    def book_venue(self, date: str)-> str:
        return f"Venue booked for {date}"
    
venue_booking = VenueBooking()
print(venue_booking.book_venue("4/13/2024"))
    

class CateringService:
    """
    Sub-system for handeling catering orders
    """
    def arrange_catering(self, menu: str)-> str:
        return f"Catering order for {menu}"


class Notifications:
    """
    Subsystems for  handeling noticfications
    """
    def send_invitation(self) -> str:
        return "Invitation sent"

class PeopleCount:
    def person_count(self, people: int)-> int:
        return f"You have {people} people coming to the event!"




class EventManager:
    """Facade class which simpligies the interactoin with various management systems"""
    def __init__(self) -> None:
        self.venue_booking = VenueBooking()
        self.catering_service = CateringService()
        self.notification_system = Notifications()
        self.people_count = PeopleCount()

    def organize_event(self, date: str, menu: str, people: int)-> str:
        """A method to arganize all the events by coordinating with difference services"""

        results = []
        results.append(self.venue_booking.book_venue(date))
        results.append(self.catering_service.arrange_catering(menu))
        results.append(self.notification_system.send_invitation())
        results.append(self.people_count.person_count(people))
        return "\n".join(results)



def client_code(event_manager: EventManager) -> None:
    print(event_manager.organize_event( "2024-03-15", "Carnivore, Gluten Free", 25 ))


if __name__ == "__main__":
    event_manager = EventManager()
    client_code(event_manager)

