import helper
from django.core.management.base import BaseCommand
from django.conf import settings

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')


VENDOR_STATICFILES ={
    'flowbite.min.css':"https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css",
    'flowbite.min.js':"https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js",
    'flowbite.min.js.map': "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js.map",
}

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Downloading vendor files...')
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            outpath = STATICFILES_VENDOR_DIR / name
            dl_success = helper.download_to_local(url, outpath)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download {url} to {outpath}') 
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS('Downloaded all vendor files'))
        else:
            self.stdout.write(self.style.ERROR('Failed to download all vendor files'))

        