from django.db import models

class Tenant(models.Model):
    tenant_id=models.CharField(max_length=200)
    tenant_name=models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s' %(self.tenant_id,self.tenant_name)

class StackUser(models.Model):
    user_id = models.CharField(max_length=200)
    user_name=models.CharField(max_length=200)
    tenant_id = models.ForeignKey(Tenant)
    
    def __unicode__(self):  
        return u'%s' % (self.user_id)

class MetersCounter(models.Model):
    meter_name = models.CharField(max_length=200)
    user_id = models.ForeignKey(StackUser)
    counter_volume = models.TextField(blank=True,null=True,default='0.0')
    unit = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    
    def __unicode__(self):  
        return u' %s' % (self.counter_volume)


class PriceLoop(models.Model):
    price = models.FloatField()
    timestamp = models.DateTimeField()
    tenant_id = models.ForeignKey(Tenant)
    
    def __unicode__(self):  
        return u'%s %s %s' % (self.tenant_id, self.price, self.timestamp)
    
class PricingFunc(models.Model):
    user_id = models.ForeignKey(StackUser)
    param1 = models.CharField(max_length=200, blank=True, null=True)
    sign1 = models.CharField(max_length=5,blank=True, null=True)
    param2 = models.CharField(max_length=200,blank=True, null=True)
    sign2 = models.CharField(max_length=5,blank=True, null=True)
    param3 = models.CharField(max_length=200,blank=True, null=True)
    sign3 = models.CharField(max_length=5,blank=True, null=True)
    param4 = models.CharField(max_length=200,blank=True, null=True)
    sign4 = models.CharField(max_length=5,blank=True, null=True)
    param5 = models.CharField(max_length=200,blank=True, null=True)
    currency=models.CharField(max_length=200,default='CHF')
    unit=models.CharField(max_length=200,default='0.01', null=True,blank=True)
    
    class Meta:  
        app_label = 'main_menu'
    
    def __unicode__(self):  
        return u'%s %s %s %s %s %s %s %s %s %s %s %s' % (self.user_id, self.param1, self.sign1, self.param2, self.sign2, self.param3, self.sign3, self.param4, self.sign4, self.param5,self.currency,self.unit)    
    

    
class Udr(models.Model):
    user_id = models.ForeignKey(StackUser)
    timestamp = models.DateTimeField()
    pricing_func_id = models.ForeignKey(PricingFunc)
    param1 = models.CharField(max_length=200,blank=True, null=True)
    param2 = models.CharField(max_length=200,blank=True, null=True)
    param3 = models.CharField(max_length=200,blank=True, null=True)
    param4 = models.CharField(max_length=200,blank=True, null=True)
    param5 = models.CharField(max_length=200,blank=True, null=True)  
    
    #def __unicode__(self):  
     #   return u'%s %s %s %s %s %s ' % (self.user_id, self.param1, self.param2, self.param3, self.param4, self.param5)        
    
class PriceCdr(models.Model):
    price = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField() 
    user_id = models.ForeignKey(StackUser,related_name='+')
    pricing_func_id = models.ForeignKey(PricingFunc,related_name='+')
    
    def __unicode__(self):  
        return u'%s %s %s ' % (self.user_id, self.price, self.timestamp) 
        
class PriceDaily(models.Model):
    price = models.FloatField(blank=True, null=True) 
    timestamp = models.DateTimeField() 
    tenant_id = models.ForeignKey(Tenant) 
    pricing_func_id = models.ForeignKey(PricingFunc)   
    
    def __unicode__(self):  
        return u'%s %s %s  ' % (self.tenant_id, self.price, self.timestamp)    
       

  
    

