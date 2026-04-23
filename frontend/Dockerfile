FROM node:18-alpine

WORKDIR /app

# Install only production deps
COPY package*.json ./
RUN npm ci --omit=dev

COPY . .

# Non-root user
RUN adduser -D appuser
USER appuser

EXPOSE 3000

CMD ["npm", "start"]

HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD wget -qO- http://localhost:3000/health || exit 1