#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-7-oracle

cd /tmp

wget http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-amd64.tar.gz && \
gunzip -c jai-1_1_3-lib-linux-amd64.tar.gz | tar xf - && \
mv /tmp/jai-1_1_3/lib/*.jar $JAVA_HOME/jre/lib/ext/ && \
mv /tmp/jai-1_1_3/lib/*.so $JAVA_HOME/jre/lib/amd64/ && \
rm /tmp/jai-1_1_3-lib-linux-amd64.tar.gz && \
rm -r /tmp/jai-1_1_3

wget http://download.java.net/media/jai-imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64.tar.gz && \
gunzip -c jai_imageio-1_1-lib-linux-amd64.tar.gz | tar xf - && \
mv /tmp/jai_imageio-1_1/lib/*.jar $JAVA_HOME/jre/lib/ext/ && \
mv /tmp/jai_imageio-1_1/lib/*.so $JAVA_HOME/jre/lib/amd64/ && \
rm /tmp/jai_imageio-1_1-lib-linux-amd64.tar.gz && \
rm -r /tmp/jai_imageio-1_1
