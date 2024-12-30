from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    date_added = models.DateTimeField('date added')
    
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['date_added',]
    
    def __str__(self):
        return self.name
    
    
PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product_img/one', null=True)
    image2 = models.ImageField(upload_to='product_img/two', null=True)
    image3 = models.ImageField(upload_to='product_img/three', null=True)
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'products'
        ordering = ['date_added',]
        
    def get_category(self):
        return self.category.name
        
    def get_image_1(self):
        if self.image1:
            return "https://api-gbstoregh.xyz" + self.image1.url
        return ''
    
    def get_image_2(self):
        if self.image2:
            return "https://api-gbstoregh.xyz" + self.image2.url
        return ''
    
    def get_image_3(self):
        if self.image3:
            return "https://api-gbstoregh.xyz" + self.image3.url
        return ''
        
    
    def __str__(self):
        return self.title