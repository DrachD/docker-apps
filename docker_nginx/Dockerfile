# We use alpine because this image has the smallest size
FROM nginx:alpine
LABEL maintainer="drachdmitriy21@gmail.com"
COPY index.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
