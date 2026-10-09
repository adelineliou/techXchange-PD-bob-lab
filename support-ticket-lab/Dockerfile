FROM nginx:alpine

# Reconfigure nginx to listen on 8080 (required by Code Engine)
RUN sed -i 's/listen\s*80;/listen 8080;/g' /etc/nginx/conf.d/default.conf

# Copy the lab guide HTML as the default page
COPY LAB_GUIDE.html /usr/share/nginx/html/index.html

# Copy screenshots directory
COPY lab-screenshots/ /usr/share/nginx/html/lab-screenshots/

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
