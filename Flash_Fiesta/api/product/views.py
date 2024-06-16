from rest_framework.decorators import api_view
from store.models import Product
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer


# @api_view(["GET"])
# def ProductView (request):
#   productModel = ProductSerializer()
#   ProductDetails = []
#   if productModel:
#     print(productModel)
#     for i in productModel:
#         product_detail = {
#             'ProductName': i.ProductName,
#             'ProductID': i.ProductID,
#             # 'ProductImage': str(i.ProductImage) 
#         }
#         ProductDetails.append(product_detail)

#     respoonse_data ={'Status':6000,'data' : ProductDetails}
#   else:
#     respoonse_data ={'Status':6001,'data' : ProductDetails}
  
#   return Response (respoonse_data,status=status.HTTP_200_OK)

@api_view(["GET"])
def ProductView(request):
    try:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        response_data = {'Status': 6000, 'data': serializer.data}
    except Exception as e:
        print(f"Error fetching product details: {e}")
        response_data = {'Status': 6001, 'data': []}

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(["POST"])
def Create_Product(request):
        data = request.data
        ProductName = data['ProductName']
        try:
            Description = data['Description']
        except:
            Description = ''
        try:
            ProductImage = data['ProductImage']
        except:
            ProductImage = ''

        Qty = data['Qty']
        Rate = data['Rate']


        if ProductName:
            CreateProduct =  Product.objects.create(
                ProductName = ProductName,
                ProductDescription = Description,
                ProductImage = ProductImage,
                ProductQuantity = Qty,
                ProductPrice = Rate
            )
            CreateProduct.save()
            response_data = {'Status': 6000, 'data': 'Product created successfully'}
        else:
            response_data = {'Status': 6001, 'data': 'Provide valid data'}
        return Response(response_data,status=status.HTTP_200_OK)

        