from playsound import playsound


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:
            # Save the model
            self.model.email = email
            self.model.save()

            # Show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # Show an error message
            self.view.show_error(error)
    
    def play_music(self):
        """
        Play music
        :return:
        """
        print("controller: Play Buttone CLICKED!")
        playsound('music/Bad_Bunny_WHERE_SHE_GOES.mp3')
