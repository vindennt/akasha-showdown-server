package user

import (
	"github.com/vindennt/akasha-showdown-server/src/config"
)

type UserService struct {
    cfg *config.Config
    // db *sql.DB // database
}

func NewUserService(cfg *config.Config /*, db *sql.DB */) *UserService {
    return &UserService{
        cfg: cfg,
        // db: db,
    }
}

func (user *UserService) CreateUser(name string, email string) error {
    // TODO:
    return nil
}

func (user *UserService) GetUser(id string) (*User, error) {
	// TODO:
    return &User{ID: id, Name: "Sample"}, nil
}
