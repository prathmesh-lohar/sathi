# from django.contrib.auth.base_user import BaseUserManager


# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def create_user(self,username,password=None, **extra_fields):
#         if not username:
#             raise ValueError('username required')
#         user = self.model(related_officer=related_officer, **extra_fields)
#         user.set_password(password)
#         user.save(using = self.db)
#         return user

#     def create_superuser(self,username,password=None, **extra_field):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)

#         return self.create_user(related_officer, password,extra_fields)