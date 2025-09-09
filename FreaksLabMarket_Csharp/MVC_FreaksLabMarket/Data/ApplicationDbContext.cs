using Microsoft.EntityFrameworkCore;
using MVC_FreaksLabMarket.Models;

namespace MVC_FreaksLabMarket.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
        {
            
        }

        public DbSet<Category> Category { get; set; }
    }
}
