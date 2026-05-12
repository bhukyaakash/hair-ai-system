"""Run All Model Training Scripts Sequentially"""

import subprocess
import sys
import os
from datetime import datetime
import json

# Ensure we're in the backend directory
os.chdir(os.path.dirname(__file__))
os.chdir('..')

print("="*70)
print("HAIR AI SYSTEM - COMPLETE MODEL TRAINING PIPELINE")
print("="*70)
print(f"Start Time: {datetime.now().isoformat()}")
print("="*70)

# Models to train
models_to_train = [
    "train_face_shape",
    "train_hairstyle",
    "train_hair_health",
    "train_disease_detector"
]

results = {
    "start_time": datetime.now().isoformat(),
    "models": {}
}

failed_models = []
successful_models = []

for i, model in enumerate(models_to_train, 1):
    print(f"\n{'#'*70}")
    print(f"[{i}/{len(models_to_train)}] Running {model}...")
    print(f"{'#'*70}\n")
    
    model_start = datetime.now()
    
    try:
        # Run the training script
        result = subprocess.run(
            [sys.executable, "-m", f"training.{model}"],
            capture_output=False,
            timeout=3600  # 1 hour timeout per model
        )
        
        model_duration = datetime.now() - model_start
        
        if result.returncode == 0:
            print(f"\n✅ {model} COMPLETED SUCCESSFULLY")
            successful_models.append(model)
            results["models"][model] = {
                "status": "completed",
                "duration": str(model_duration),
                "return_code": 0
            }
        else:
            print(f"\n⚠️  {model} finished with non-zero return code: {result.returncode}")
            failed_models.append(model)
            results["models"][model] = {
                "status": "completed_with_warnings",
                "duration": str(model_duration),
                "return_code": result.returncode
            }
            
    except subprocess.TimeoutExpired:
        print(f"\n❌ {model} TIMEOUT (exceeded 1 hour)")
        failed_models.append(model)
        results["models"][model] = {
            "status": "timeout",
            "duration": "3600+"
        }
    except Exception as e:
        print(f"\n❌ {model} FAILED with error: {e}")
        failed_models.append(model)
        results["models"][model] = {
            "status": "failed",
            "error": str(e)
        }

# Final summary
print("\n" + "="*70)
print("TRAINING PIPELINE SUMMARY")
print("="*70)
print(f"Total Models: {len(models_to_train)}")
print(f"✅ Successful: {len(successful_models)}")
print(f"⚠️  Failed/Warnings: {len(failed_models)}")
print(f"End Time: {datetime.now().isoformat()}")
print("="*70)

if successful_models:
    print("\n✅ SUCCESSFUL MODELS:")
    for model in successful_models:
        print(f"  • {model}")

if failed_models:
    print("\n⚠️  MODELS WITH ISSUES:")
    for model in failed_models:
        print(f"  • {model}")

# Save results to JSON
results["end_time"] = datetime.now().isoformat()
results["summary"] = {
    "total": len(models_to_train),
    "successful": len(successful_models),
    "failed": len(failed_models),
    "success_rate": f"{(len(successful_models)/len(models_to_train))*100:.1f}%"
}

with open("logs/training_results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\n📊 Results saved to logs/training_results.json")

# Check for generated models
print("\n" + "="*70)
print("MODEL FILES GENERATED")
print("="*70)

model_dir = "app/ml/saved_models"
if os.path.exists(model_dir):
    files = os.listdir(model_dir)
    if files:
        print(f"\n📁 {model_dir}:")
        for file in sorted(files):
            file_path = os.path.join(model_dir, file)
            size = os.path.getsize(file_path) / (1024*1024)  # MB
            print(f"  ✓ {file} ({size:.2f} MB)")
    else:
        print(f"\n⚠️  No files found in {model_dir}")
else:
    print(f"\n⚠️  Directory {model_dir} does not exist")

print("\n" + "="*70)
print("NEXT STEPS:")
print("="*70)
print("1. Review model metrics: app/ml/saved_models/*_metrics.json")
print("2. Start API server: python -m app.main")
print("3. Test API endpoints")
print("4. Deploy to production")
print("="*70)

# Exit with appropriate code
sys.exit(0 if len(failed_models) == 0 else 1)
