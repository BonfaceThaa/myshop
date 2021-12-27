from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet


class ProductImageFormset(BaseInlineFormSet):
    def clean(self):
        """
        InlineFormSet function that validates each product has at least one Primary image in the case it has images.
        :return: validation error if product has images and none of primary type
        """
        super(ProductImageFormset, self).clean()
        primary_images = 0
        other_images = 0
        for form in self.forms:
            image_type = form.cleaned_data.get('image_type')
            if image_type == 'SEC' or image_type == 'OTH':
                other_images += 1
            elif image_type == 'PRI':
                primary_images += 1

        if other_images > 0 and primary_images == 0:
            raise ValidationError('Every product requires a Primary image first. Please provide at least one image'
                                  ' of type Primary before adding other images of secondary or others type.')
