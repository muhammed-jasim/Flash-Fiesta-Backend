from rest_framework.decorators import api_view
from store.models import Product
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def ProductView (request):
  productModel = Product.objects.all()
  ProductDetails = []
  if productModel:
    print(productModel)
    for i in productModel:
        product_detail = {
            'ProductName': i.ProductName,
            'ProductID': i.ProductID,
            'ProductImage': str(i.ProductImage) 
        }
        ProductDetails.append(product_detail)

    respoonse_data ={'Status':6000,'data' : ProductDetails}
  else:
    respoonse_data ={'Status':6001,'data' : ProductDetails}
  
  return Response (respoonse_data,status=status.HTTP_200_OK)