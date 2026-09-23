## Docker Basics

Docker packages applications into containers — lightweight, portable units.

### Key commands
```bash
docker run hello-world              # Run a test container
docker ps                            # List running containers
docker ps -a                         # List all containers
docker images                        # List local images
docker stop <container_id>           # Stop a container
docker rm <container_id>             # Remove a container
docker rmi <image_id>                # Remove an image
```

**Container ≠ VM** — containers share the host kernel.

## Git Basics

```bash
git init                        # Initialize repo
git add .                       # Stage all changes
git commit -m 'Initial commit'  # Commit
git status                      # Check status
git log --oneline               # Compact log
git diff                        # Show unstaged changes
git diff --staged               # Show staged changes
```

### Three areas
Working Directory → Staging Area → Repository

## Nginx Basics

Nginx is a high-performance web server and reverse proxy.

### Basic config
```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        root /var/www/html;
        index index.html;
    }

    location /api {
        proxy_pass http://localhost:3000;
    }
}
```

```bash
sudo nginx -t           # Test config
sudo systemctl reload nginx  # Reload
```

## Essential Linux Commands

```bash
# File operations
ls -la                  # List all with details
cp -r src/ dest/        # Copy directory
mv old.txt new.txt      # Rename/move
rm -rf dir/             # Remove directory
find . -name '*.py'     # Find files

# Text processing
cat file.txt            # Display file
grep -r 'pattern' .     # Search recursively
wc -l file.txt          # Count lines
head -20 file.txt       # First 20 lines
tail -f log.txt         # Follow log file

# System
ps aux                  # List processes
top                     # Process monitor
df -h                   # Disk usage
chmod 755 script.sh     # Set permissions
```
