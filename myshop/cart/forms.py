from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # 可以在 PRODUCT_QUANTITY_CHOICES 的範圍內選擇數量
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    # 如果為false則在購物車原數量基礎上增加quantity, true則將數量設置為quantity
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
