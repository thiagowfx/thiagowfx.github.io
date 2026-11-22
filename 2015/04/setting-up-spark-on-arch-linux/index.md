---
title: "Setting up Spark on Arch Linux"
url: https://perrotta.dev/2015/04/setting-up-spark-on-arch-linux/
last_updated: 2026-11-22
---


First things first: install OpenJDK (version 8 is the better one at the time of
this post) and Scala. This should be pretty standard. But if you really need
some orientation, then check out [our Wiki](https://wiki.archlinux.org/index.php/Scala).

```shell
sudo pacman -S scala scala-docs scala-sources
```

I'm not listing any JDKs here because there are several variants of it to choose
from. I personally use `jdk8-openjdk-infinality` to benefit from the
[infinality](https://wiki.archlinux.org/index.php/Infinality) font patchset.

Now, check out if you're good to go:

```text
$ scala
Welcome to Scala version 2.11.6 (OpenJDK 64-Bit Server VM, Java 1.8.0_40).
Type in expressions to have them evaluated.
Type :help for more information.

scala> println("hello world")
hello world
```

Now, let's grab the
[apache-spark](https://aur.archlinux.org/packages/apache-spark/) package from
the AUR. Untar it and do a

**Edit**: actually, I recommend this `PKGBUILD` that I improved, based on the one
from the AUR: (note: this will be deprecated one day...)

```bash
# Maintainer: Franois Garillot ("huitseeker")
# Contributor: Christian Krause ("wookietreiber") <kizkizzbangbang@gmail.com>
# Contributor: Thiago Perrotta ("thiagowfx")

pkgname=apache-spark
pkgver=1.3.1
pkgrel=2
pkgdesc="fast and general engine for large-scale data processing"
arch=('i686' 'x86_64')
url="http://spark.apache.org/"
license=('Apache')
depends=('maven' 'java-environment>=6' 'scala' 'python2>=2.7')
install=$pkgname.install
source=("http://d3kbcqa49mib13.cloudfront.net/spark-$pkgver.tgz"
        "$pkgname-standalone.service"
        'spark-env.sh')
md5sums=('5ae47bffe0e88c3ccf26e70a72791070'
         'bb7d8b85366e6f9cc0b2777eaea161a8'
         '0913001583e607849270090555dbd309')
backup=("etc/$pkgname/spark-env.sh")

prepare() {
  cd "$srcdir/spark-$pkgver"
  sed -i "s|pid=$SPARK_PID_DIR/spark-$SPARK_IDENT_STRING-$command-$instance.pid|pid=/var/lib/$pkgname/spark-daemon.pid|" sbin/spark-daemon.sh
}

build() {
  cd "$srcdir/spark-$pkgver"

  export MAVEN_OPTS="-Xmx2g -XX:MaxPermSize=512M -XX:ReservedCodeCacheSize=512m"
  dev/change-version-to-2.11.sh
  mvn -Dscala-2.11 -DskipTests -Dmaven.repo.local=/tmp clean package
}

package() {
  cd "$srcdir/spark-$pkgver"

  install -d "$pkgdir/usr/bin" "$pkgdir/usr/share"

  cp -r "$srcdir/spark-$pkgver" "$pkgdir/usr/share/$pkgname/"

  for f in spark-{class,sql,shell,submit}; do
      echo -e "#!/bin/sh\ncd /usr/share/$pkgname/bin/\n./$f" > "$pkgdir/usr/bin/$f"
      chmod +x "$pkgdir/usr/bin/$f"
  done

  install -Dm644 "$srcdir/$pkgname-standalone.service" "$pkgdir/usr/lib/systemd/system/$pkgname-standalone.service"
  install -Dm644 "$srcdir/spark-env.sh" "$pkgdir/etc/$pkgname/spark-env.sh"

  cd "$pkgdir/usr/share/$pkgname/conf"
  ln -sf "/etc/$pkgname/spark-env.sh" .
}
```

```shell
$ makepkg -si
```

And now wait. Spark is built with `maven`, so it will pull several dependencies
then compile them; maven is the equivalent of [cmake](http://www.cmake.org/) in
the Java world.

Why is this here? To show people from other distros how easy it is to install
"uncommon" software on Arch. And hey, if the software is not packaged, then it
is (usually) easy to do that too; just request this on the appropriate
[subforum](https://bbs.archlinux.org/viewforum.php?id=38). Or, better yet,
[learn](https://wiki.archlinux.org/index.php/Makepkg) to do that yourself.

**Update(2026-11-22)**: And now one can simply use LLMs to do so.

