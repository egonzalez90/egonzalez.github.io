--- layout: post title: 'TIP: Proximo fsck' date: 2014-08-29
15:00:30.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Linux tags: - "-l" -
"/dev/sda1" - filesystem check - fsck - intervalo - linux - proximo -
tip - tune2fs meta: \_edit_last: '2' \_login_radius_meta: '0'
kopa_resolution_total_view: '5' snap_MYURL: '' snapEdIT: '1' snapFB: N;
snap_isAutoPosted: '1' snapTW: N; post_views_count: '1'
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1566909466;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:605;}i:1;a:1:{s:2:"id";i:662;}i:2;a:1:{s:2:"id";i:781;}}}}
author: login: egongu90 email: egongu90@hotmail.com display_name: Editor
first_name: '' last_name: '' permalink: "/tip-proximo-fsck/" ---

   tune2fs -l /dev/dispositivo\*

\*dispositivo puede ser sda1, sda2, sdb1, etc

Entre los datos que te muestra el comando, puedes ver el intervalo de
chequeo del fs, ultimo fsck, la cuenta de las veces montado y el máximo
de las veces montado el fs hasta que se haga un fsck
