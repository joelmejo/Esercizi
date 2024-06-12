from privileges import Privileges
from admin import Admin

privileges = Privileges(["can add post", "can delete post", "can ban user"])
admin = Admin("John", "Doe", 25, privileges)
admin.privileges.show_privileges()