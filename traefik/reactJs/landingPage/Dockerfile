# Use an official Node.js runtime as a parent image
FROM node:alpine3.20 as build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY ./package*.json ./

# Install dependencies
RUN npm install

# Copy the entire application code to the working directory
COPY . .

# Build the React application
RUN npm run build

# Stage 2: Serve the built React application with a lightweight HTTP Server
FROM node:alpine3.20

# Copy the build output from the previous stage
COPY --from=build /app/dist /app/build

WORKDIR /app
# Install a simple HTTP server for serving static content
RUN npm install -g http-server

# Make port 5173 available to the world outside this container
EXPOSE 5173

# Run the HTTP server to serve the built React app
CMD ["http-server", "-p", "5173", "build"]