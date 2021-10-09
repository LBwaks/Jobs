from django.db import models
from autoslug import AutoSlugField
from django.conf import settings
from  ckeditor.fields import RichTextField
from django.urls import reverse
from PIL import Image

class Category(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,editable=False,on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description =RichTextField()
    created_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse("artist_category",kwargs={'slug':self.slug})

class Tag(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,editable=False,on_delete=models.CASCADE,null=False,related_name='blog_tag_user')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='blog_category_tag')  
    name = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description =RichTextField()
    created_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse("home")

# Create your models here.
class Job(models.Model):
    Mombasa = 'Mombasa'
    Kwale= 'Kwale'
    Kilifi= 'Kilifi'
    TanaRiver= 'Tana River'
    Lamu= 'Lamu'
    TaitaTaveta= 'Taita-Taveta'
    Garissa ='Garissa'
    Wajir= 'Wajir'
    Mandera= 'Mandera'
    Marsabit= 'Marsabit'
    Isiolo= 'Isiolo'
    MERU= 'MERU'
    TharakaNithi= 'Tharaka-Nithi'
    Embu= 'Embu'
    Kitui ='Kitui'
    Machakos= 'Machakos'
    Makueni= 'Makueni'
    Nyandarua= 'Nyandarua'
    Nyeri= 'Nyeri'
    Kirinyaga='Kirinyaga'
    Muranga="Muranga"
    Kiambu= 'Kiambu'
    Turkana ='Turkana'
    WestPokot='West Pokot'
    Samburu= 'Samburu'
    TransNzoia ='Trans Nzoia'
    UasinGishu= 'Uasin Gishu'
    ElgeyoMarakwet= 'Elgeyo-Marakwet'
    Nandi ='Nandi'
    Baringo= 'Baringo'
    Laikipia ='Laikipia'
    Nakuru= 'Nakuru'
    Narok= 'Narok'
    Kajiado= 'Kajiado'
    Kericho= 'Kericho'
    Bomet= 'Bomet'
    Kakamega ='Kakamega'
    Vihiga= 'Vihiga'
    Bungoma= 'Bungoma'
    Busia= 'Busia'
    Siaya= 'Siaya'
    Kisumu ='Kisumu'
    HomaBay= 'Homa Bay'
    Migori= 'Migori'
    Kisii= 'Kisii'
    Nyamira= 'Nyamira'
    Nairobi= 'Nairobi'

    county_choice= [
        (Mombasa, 'Mombasa'),
        (Kwale, 'Kwale'),
        (Kilifi, 'Kilifi'),
        (TanaRiver, 'Tana River'),
        (Lamu, 'Lamu'),
        (TaitaTaveta, 'Taita-Taveta'),
        (Garissa ,'Garissa'),
        (Wajir, 'Wajir'),
        (Mandera, 'Mandera'),
        (Marsabit, 'Marsabit'),
        (Isiolo, 'Isiolo'),
        (MERU, 'Meru'),
        (TharakaNithi, 'Tharaka-Nithi'),
        (Embu, 'Embu'),
        (Kitui ,'Kitui'),
        (Machakos, 'Machakos'),
        (Makueni, 'Makueni'),
        (Nyandarua, 'Nyandarua'),
        (Nyeri, 'Nyeri'),
        (Kirinyaga,'Kirinyaga'),
        (Muranga,"Murang'a"),
        (Kiambu, 'Kiambu'),
        (Turkana ,'Turkana'),
        (WestPokot,' West Pokot'),
        (Samburu, 'Samburu'),
        (TransNzoia ,'Trans Nzoia'),
        (UasinGishu, 'Uasin Gishu'),
        (ElgeyoMarakwet, 'Elgeyo-Marakwet'),
        (Nandi ,'Nandi'),
        (Baringo, 'Baringo'),
        (Laikipia ,'Laikipia'),
        (Nakuru, 'Nakuru'),
        (Narok, 'Narok'),
        (Kajiado, 'Kajiado'),
        (Kericho, 'Kericho'),
        (Bomet, 'Bomet'),
        (Kakamega ,'Kakamega'),
        (Vihiga, 'Vihiga'),
        (Bungoma, 'Bungoma'),
        (Busia, 'Busia'),
        (Siaya, 'Siaya'),
        (Kisumu ,'Kisumu'),
        (HomaBay, 'Homa Bay'),
        (Migori, 'Migori'),
        (Kisii, 'Kisii'),
        (Nyamira, 'Nyamira'),
        (Nairobi, 'Nairobi'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    tag = models.ForeignKey(Tag,verbose_name="Tag",on_delete=models.CASCADE)
    description = RichTextField()
    done_by_date = models.DateTimeField(auto_now_add=False)
    done_at_date = models.DateTimeField(auto_now_add=False)
    location_county =models.CharField( choices=county_choice, max_length=20,  default=Nairobi)
    location_town = models.CharField(max_length=250)
    location_address_location = models.CharField(max_length=250)
    location_exact_job_location = models.CharField(max_length=250)
    job_reference =models.CharField(max_length=250,blank=True,null=True)
    status = models.CharField(max_length=250,blank=True,null=True)
    is_featured = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    image =models.ImageField(upload_to='jobs/job_images/',default='job_images/jobs.jpg',blank=True,null=True)
    video =models.FileField(upload_to='jobs/job_videos/',blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_details", kwargs={"slug": self.slug})
    

