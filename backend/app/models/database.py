"""SQLAlchemy Database Models"""

from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

Base = declarative_base()


class User(Base):
    """User model"""
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    assessments = relationship("FaceShapeAssessment", back_populates="user")
    appointments = relationship("Appointment", back_populates="user")
    health_assessments = relationship("HairHealthAssessment", back_populates="user")


class FaceShapeAssessment(Base):
    """Face shape assessment model"""
    __tablename__ = "face_shape_assessments"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    face_shape = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    image_path = Column(String, nullable=True)
    analysis_metadata = Column(Text, nullable=True)  # JSON
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="assessments")


class HairstyleRecommendation(Base):
    """Hairstyle recommendation model"""
    __tablename__ = "hairstyle_recommendations"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    assessment_id = Column(String, ForeignKey("face_shape_assessments.id"), nullable=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    hairstyle_name = Column(String, nullable=False)
    category = Column(String, nullable=False)  # modern, futuristic, old, present, old_age
    compatibility_score = Column(Float, nullable=False)
    image_url = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class HairHealthAssessment(Base):
    """Hair health assessment model"""
    __tablename__ = "hair_health_assessments"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    health_score = Column(Float, nullable=False)
    hair_thickness = Column(String, nullable=False)  # thin, normal, thick
    hair_condition = Column(String, nullable=False)  # dry, normal, oily
    scalp_condition = Column(String, nullable=False)
    issues_detected = Column(Text, nullable=True)  # JSON array
    recommendations = Column(ARRAY(String), nullable=True)
    image_paths = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="health_assessments")


class Stylist(Base):
    """Stylist model"""
    __tablename__ = "stylists"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    specialization = Column(String, nullable=True)
    experience_years = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    appointments = relationship("Appointment", back_populates="stylist")


class Appointment(Base):
    """Appointment model"""
    __tablename__ = "appointments"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    stylist_id = Column(String, ForeignKey("stylists.id"), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    appointment_time = Column(String, nullable=False)
    service_type = Column(String, nullable=False)  # haircut, coloring, styling, treatment
    status = Column(String, default="scheduled")  # scheduled, completed, cancelled
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="appointments")
    stylist = relationship("Stylist", back_populates="appointments")
