sudo ufw app info "Apache Full"

sudo ufw allow in "Apache Full"

sudo chown :www-data sathi
sudo chown :www-data sathi/db.sqlite3
sudo chown :www-data sathi/static/

sudo chown :www-data sathi/static/admin/
sudo chown :www-data sathi/media/
sudo chown :www-data sathi/media/documents
sudo chown :www-data sathi/media/dp
sudo chown :www-data sathi/media/gallery




sudo chmod -R 775 vdf/

sudo chmod -R 775 sathi/db.sqlite3
sudo chmod -R 775 sathi/static/
sudo chmod -R 775 sathi/static/admin/
sudo chmod -R 775 sathi/media/
sudo chmod -R 775 sathi/media/documents
sudo chmod -R 775 sathi/media/dp
sudo chmod -R 775 sathi/media/gallery


 sudo systemctl restart apache2